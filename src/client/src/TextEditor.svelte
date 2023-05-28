<script lang="ts">
    import CircularProgress from "@smui/circular-progress";

    import { quill } from "svelte-quill";
    import Quill from "quill/core";

    import { onMount } from "svelte";

    let correctedText = "";
    let correctedMdText = "";
    let inputText = "";
    let processing = false;

    const options = {
        placeholder: "Paste your text...",
        modules: {
            toolbar: "#toolbar",
        },
        theme: "snow",
    };
    let content = { html: "", text: "" };

    async function critiqueText() {
        processing = true;
        let response = await fetch("./critique", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                text: inputText,
            }),
        });

        // response.status === 200;
        let corrected = await response.json();
        processing = false;
        correctedText = corrected?.suggestion?.suggested_text;

        correctedMdText = corrected?.suggestion?.suggested_markdown;
        correctedMdText = correctedMdText ? correctedMdText : correctedText;
    }

    // this element will be externally bound to the quill HTML instance
    let quillElement;

    onMount(() => {
        // see https://github.com/kevmodrome/svelte-quill/issues/4
        const quillInstance = Quill.find(quillElement);
        quillInstance?.setText(inputText);

        var toolbar = quillInstance.getModule("toolbar");
        // toolbar.addHandler('wb-critique', critiqueText); // doesn't work

        var customButton = document.querySelector("#wb-critique");
        customButton.addEventListener("click", function () {
            critiqueText();
        });
    });
</script>

<svelte:head>
    <link href="//cdn.quilljs.com/1.3.6/quill.snow.css" rel="stylesheet" />
</svelte:head>

<div id="toolbar">
    <button id="wb-critique">✨</button>
</div>

<div
    class="editor"
    id="quill-editor-container"
    bind:this={quillElement}
    use:quill={options}
    on:text-change={(e) => {
        content = e.detail;
        inputText = content.html;
    }}
/>

<hr />

{#if processing}
    <div style="display: flex; justify-content: center">
        <CircularProgress
            class="my-four-colors"
            style="height: 32px; width: 32px;"
            indeterminate
            fourColor
        />
    </div>
{:else}
    {#if correctedText}
        <div>
            <div class="mdc-typography--body1">Corrected Text</div>
            <textarea>{correctedText}</textarea>
        </div>
    {/if}

    {#if correctedMdText}
        <div>
            <div class="mdc-typography--body1">Corrected Markdown Text</div>
            <textarea>{correctedMdText}</textarea>
        </div>
    {/if}
{/if}

<style lang="scss">
    // Import all the styles for the classes.
    @use "@material/typography/mdc-typography";
    // The following classes become available:
    //   mdc-typography--headline1
    //   mdc-typography--headline2
    //   mdc-typography--headline3
    //   mdc-typography--headline4
    //   mdc-typography--headline5
    //   mdc-typography--headline6
    //   mdc-typography--subtitle1
    //   mdc-typography--subtitle2
    //   mdc-typography--body1
    //   mdc-typography--body2
    //   mdc-typography--caption
    //   mdc-typography--button
    //   mdc-typography--overline
    //   mdc-typography--body1

    // Import the mixins.
    @use "@material/typography/mixins" as typography;

    textarea {
        width: 100%;
        height: 200px;
    }
    #quill-editor-container {
        height: 10em;
    }
</style>
