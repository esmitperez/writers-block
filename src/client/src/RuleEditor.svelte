<script lang="ts">
	import { createStyleRule} from './utils';
    import { currentText } from './rule_store';
</script>

<form on:submit|preventDefault={createStyleRule}>
    <div>
        Add Rule
        <textarea bind:value={$currentText} id="stickyText" />
    </div>
    <button type="submit">⚡️ New Rule</button>
</form>

<style>
    textarea {
        width: 100%;
        min-height: 5em;
    }
</style>
