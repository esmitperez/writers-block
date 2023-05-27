<script>
    let currentText = "";
    let correctedText = ""

    async function critiqueText() {
        let currentTextValue = "";

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
</script>

<form on:submit|preventDefault={critiqueText}>
    <div>
        Text to Correct
        <textarea bind:value={currentText} id="stickyText" />
    </div>
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
</style>
