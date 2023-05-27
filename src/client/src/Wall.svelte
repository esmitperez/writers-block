<script>
    import StyleRule from './StyleRule.svelte';
    import { styleRuleList } from './rule_store';

  </script>
  
  {#each $styleRuleList as styleRule (styleRule.index)}
    <StyleRule index={styleRule.index} on:remove>
      <div slot='text' data-index={styleRule.index}>{styleRule.text}</div>
    </StyleRule>
  {/each}
  