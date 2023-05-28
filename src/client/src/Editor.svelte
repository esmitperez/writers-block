<script>
    import { quill } from 'svelte-quill'

	let options = { 
        placeholder: "Paste your text...", 
        modules: {
            toolbar: '#toolbar'
        },
        theme: "snow"
    }
    let content = { html: '', text: ''};


    let currentText = "this iteem is not speled corectly";
    let correctedText = ""

    async function critiqueText() {
        let response = await fetch("./critique", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                text: currentText,
            }),
        });

        // response.status === 200;
        let corrected = await response.json();
        correctedText = corrected.suggestion.suggested_text;
    }

    // var customButton = document.querySelector('#custom-button');
    // customButton.addEventListener('click', function() {
    //     critiqueText()
    // });


</script>

<svelte:head>
	<link href="//cdn.quilljs.com/1.3.6/quill.snow.css" rel="stylesheet">
</svelte:head>

<div id="toolbar">
<!-- Add buttons as you would before -->
<button class="ql-bold"></button>
<button class="ql-italic"></button>

<!-- But you can also add your own -->
<button id="first-pass-button">✨</button>
</div>
<div class="editor" id="editor-container" use:quill={options} on:text-change={e =>  {content = e.detail; currentText = content.html} }/>

Resulting HTML:

{#if correctedText}
{@html correctedText}
{/if}

<form on:submit|preventDefault={critiqueText}>
    <!-- <div>
        Text to Correct
        <textarea bind:value={currentText} id="stickyText"/>
    </div> -->
    <button type="submit">Correct</button>

    {#if correctedText}
        <div>
            <h2>Corrected Text</h2>
            <p>{correctedText}</p>
        </div>
    {/if}
</form>


<style>
    textarea {
        width: 100%;
        height: 200px;
    }
    #editor-container {
        height: 375px;
    }

</style>
