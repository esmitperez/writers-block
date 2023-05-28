<script lang="ts">
  import { styleRuleList } from "./rule_store";

  import { onMount } from "svelte";
  import { getStyleRules, deleteStyleRule } from "./utils";
  import RuleEditor from "./RuleEditor.svelte";
  import TextEditor from "./TextEditor.svelte";

  import Drawer, {
    AppContent,
    Content,
    Header,
    Title,
    Subtitle,
    Scrim,
  } from "@smui/drawer";
  import Button, { Label } from "@smui/button";

  import { mdiListBoxOutline } from "@mdi/js";
  import IconButton, { Icon } from "@smui/icon-button";
  import { Svg } from "@smui/common";
  import List, { Item, Text, Graphic, Separator, Subheader } from "@smui/list";

  onMount(async () => {
    await getStyleRules();
  });

  let open = false;
  let active = "Item1";

  function setActive(value: string) {
    active = value;
    open = false;
  }
</script>

<!-- SMUI Styles -->
<link
  rel="stylesheet"
  href="https://cdn.jsdelivr.net/npm/svelte-material-ui@6.2.0/bare.css"
/>

<div class="drawer-container">
  <Drawer variant="modal" fixed={false} bind:open>
    <Header>
      <Title>Writer's Block</Title>
      <Subtitle>Your AI-poweered style editor</Subtitle>
    </Header>
    <Content>
      <Separator />
      <Subheader tag="h6">Rules</Subheader>
      <List>
        {#each $styleRuleList as styleRule, i}
          <Item
            href="javascript:void(0)"
            on:click={() => setActive("Item" + styleRule.index)}
            activated={active === "Item" + styleRule.index}
          >
            <Text>{styleRule.name}</Text>
          </Item>
        {/each}
      </List>
    </Content>
  </Drawer>

  <!-- Don't include fixed={false} if this is a page wide drawer.
It adds a style for absolute positioning. -->
  <Scrim fixed={false} />
  <AppContent class="app-content">
    <main class="main-content">
      <div class="mdc-typography--headline2">Writer's Block</div>
      <div class="mdc-typography--subtitle1">Your AI-poweered style editor</div>

      <Button on:click={() => (open = !open)}>
        <Icon component={Svg} viewBox="0 0 24 24">
          <path fill="currentColor" d={mdiListBoxOutline} />
        </Icon><Label>View Rules</Label>
      </Button>
      <br /><br />
      <div style="height: 700px;">
        <TextEditor />
      </div>
      
      <div class="mdc-typography--body2">Created by <a href="#">Esmit Pérez</a> | Powered by 🦜⛓️ LangChain</div>

    </main>
  </AppContent>
</div>

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

  //
  // Some defaults that may be helpful to you.
  // If you just want to use these, and not the classes, you can instead just
  // @use '@material/typography/mixins' as typography, and your CSS file will be
  // smaller.
  //
  html {
    @include typography.typography("body1");
  }

  h1 {
    @include typography.typography("headline1");
  }

  h2 {
    @include typography.typography("headline2");
  }

  h3 {
    @include typography.typography("headline3");
  }

  h4 {
    @include typography.typography("headline4");
  }

  h5 {
    @include typography.typography("headline5");
  }

  h6 {
    @include typography.typography("headline6");
  }

  caption {
    @include typography.typography("caption");
  }

  code,
  pre {
    font-family: "Roboto Mono", monospace;
  }

  small {
    font-size: 0.9em;
  }

  big {
    font-size: 1.1em;
  }

  b,
  strong {
    font-weight: bold;
  }

  /** Other rules */
  /* These classes are only needed because the
    drawer is in a container on the page. */
    .drawer-container {
    position: relative;
    display: flex;
    /* height: 350px; */
    /* max-width: 600px; */
    border: 1px solid
      var(--mdc-theme-text-hint-on-background, rgba(0, 0, 0, 0.1));
    overflow: hidden;
    z-index: 0;
  }

  * :global(.app-content) {
    flex: auto;
    overflow: auto;
    position: relative;
    flex-grow: 1;
  }

  .main-content {
    overflow: auto;
    padding: 16px;
    height: 100%;
    box-sizing: border-box;
  }
</style>
