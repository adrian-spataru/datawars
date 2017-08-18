<template lang="pug">
.ui.container.marginRoute
    .ui.secondary.menu
        router-link( :to="{name: 'home.index'}").item Home
        router-link( :to="{name: 'leaderboard.index'}"  v-if="$store.state.auth.authenticated").item Leaderboard
        a(href="#",  v-if="$store.state.auth.authenticated" @click.prevent="logout").item Logout
        router-link(:to="{name: 'login.index'}" v-if="!$store.state.auth.authenticated" ).item Login 
    slot
</template>

<script>
  /* ============
   * Default Layout
   * ============
   *
   * Used for the home and account pages.
   *
   * Layouts are used to store a lot of shared code.
   * This way the app stays clean.
   */

  import authService from '@/services/auth';

  export default {
    methods: {
      logout() {
        authService.logout();
      },
    },
  };

</script>
