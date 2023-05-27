<script>
  import { onMount } from "svelte";
  import { getStyleRules } from "./utils";
  import Wall from "./Wall.svelte";
  import RuleEditor from "./RuleEditor.svelte";
  import { deleteStyleRule } from "./utils";
  import Editor from "./Editor.svelte";

  onMount(async () => {
    await getStyleRules();
  });
</script>

<!-- <RuleEditor /> -->

<Editor />

<Wall on:remove={deleteStyleRule} />
