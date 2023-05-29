<script lang="ts">
    import CircularProgress from "@smui/circular-progress";
    import IconButton, { Icon } from "@smui/icon-button";
    import Textfield from "@smui/textfield";
    import Switch from "@smui/switch";
    import FormField from "@smui/form-field";

    import Card, { Content } from "@smui/card";

    import { quill } from "svelte-quill";
    import Quill from "quill/core";

    import Prism from "./Prism.svelte";

    import { onMount } from "svelte";

    // options
    let outputMarkdown = false;
    let outputHtml = true;

    let correctedText = "";
    let correctedMdText = "";
    let inputText = "";
    let processing = false;
    let openai_api_key = "";

    const editorOptions = {
        placeholder: "Paste your text...",
        modules: {
            toolbar: "#toolbar",
        },
        theme: "snow",
    };

    let content = { html: "", text: "" };
    // this element will be externally bound to the quill HTML instances
    let quillElement;

    async function critiqueText() {
        processing = true;
        let response = await fetch("./critique", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                text: inputText,
                openai_api_key: openai_api_key,
            }),
        });

        // response.status === 200;
        let corrected = await response.json();
        processing = false;
        correctedText = corrected?.suggestion?.suggested_text;

        const quillInstance = Quill.find(quillElement);

        correctedMdText = corrected?.suggestion?.suggested_markdown?.replace(
            /\`/g,
            ""
        );
        correctedMdText = correctedMdText ? correctedMdText : correctedText;
    }

    onMount(() => {
        // see https://github.com/kevmodrome/svelte-quill/issues/4
        const quillInstance = Quill.find(quillElement);
        quillInstance?.setText(inputText);

        var customButton = document.querySelector("#critique");
        customButton.addEventListener("click", function () {
            critiqueText();
        });

        var customButton = document.querySelector("#wb-view-md");
        customButton.addEventListener("click", function () {
            outputMarkdown = !outputMarkdown;
        });
    });
</script>

<svelte:head>
    <link href="//cdn.quilljs.com/1.3.6/quill.snow.css" rel="stylesheet" />
</svelte:head>

<Textfield bind:value={openai_api_key} label="OpenAI API key" required />

<hr/>

<div id="toolbar">
    <div class="ql-format-divider" />
    <button id="critique"
        ><Icon class="material-symbols-outlined">magic_button</Icon></button
    >
</div>

<div class="layout-cell">
    <div
        class="editor"
        id="quill-editor-container"
        bind:this={quillElement}
        use:quill={editorOptions}
        on:text-change={(e) => {
            content = e.detail;
            inputText = content.html;
        }}
    />
</div>

{#if processing}
    <div style="display: flex; justify-content: center">
        <CircularProgress
            class="my-four-colors"
            style="height: 32px; width: 32px;"
            indeterminate
            fourColor
        />
    </div>
{:else if correctedText}
    <FormField>
        <Switch bind:checked={outputMarkdown} />
        <span slot="label">Show Markdown</span>
    </FormField>
    <Card>
        <div class="layout-cell">
            <div class="mdc-typography--body1">HTML</div>

            <Prism showLineNumbers={true}>
                {correctedText}
            </Prism>
        </div>
    </Card>

    {#if correctedMdText && outputMarkdown}
        <Card>
            <div class="layout-cell">
                <div class="mdc-typography--body1">Markdown Text</div>

                <Prism showLineNumbers={true}>
                    {correctedMdText}
                </Prism>
            </div>
        </Card>
    {/if}
{/if}

<style lang="scss">
    // Import all the styles for the classes.
    @use "@material/typography/mdc-typography";

    // Import the mixins.
    @use "@material/typography/mixins" as typography;

    #quill-editor-container {
        height: 10em;
    }

    .code {
        white-space: pre-wrap;
        background-color: black;
        color: white;
    }

    * :global(.card-display) {
        display: flex;
        // flex-wrap: wrap;
        // justify-content: stretch;
    }

    * :global(.card-container) {
        display: inline-flex;
        align-items: center;
        min-width: 30%;
        max-width: 50%;
        overflow-x: auto;
        background-color: var(--mdc-theme-background, #f8f8f8);
        border: 1px solid
            var(--mdc-theme-text-hint-on-background, rgba(0, 0, 0, 0.1));

        padding: 10px;

        margin-right: 10px;
        margin-bottom: 10px;
    }

    * :global(.card-container > *) {
        margin: 0 auto;
    }

    // @media (max-width: 480px) {
    //     * :global(.card-container) {
    //         margin-right: 0;
    //         padding-right: 0;
    //         padding-left: 0;
    //     }
    // }
</style>
