<script>
	import { createStyleRule} from './utils';
    import { currentText } from './rule_store';
</script>

<form on:submit|preventDefault={createStyleRule}>
    <div>
        Enter your rule...
        <textarea bind:value={$currentText} id="stickyText" />
    </div>
    <button type="submit">Style Rule +</button>
</form>

<style>
    textarea {
        width: 100%;
        height: 200px;
    }
</style>
