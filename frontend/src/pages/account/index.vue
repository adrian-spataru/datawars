<template lang="pug">
v-layout
  v-panel(contextual-style="primary")
    h1.ui.header(slot="heading")  My Account
    div(slot="body")
      p Hello
    div(slot="footer")
      p Made with love
</template>

<script>
  /* ============
   * Account Index Page
   * ============
   *
   * Page where the user can view the account information.
   */

  export default {
    components: {
      VLayout: require('@/layouts/default.vue'),
      VPanel: require('@/components/panel.vue'),
    },
  };
</script>
