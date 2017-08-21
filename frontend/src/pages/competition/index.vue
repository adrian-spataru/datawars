<template lang="pug">
v-layout
    h1.ui.header(v-text="$store.state.competition.name")
    .ui.three.item.menu
        a.item Description
        a.item Data
        router-link( :to="{name: 'leaderboard.index', params: {comp_id: $route.params.comp_id }}").item Leaderboard
</template>
<script>
  /* ============
   * Home Index Page
   * ============
   *
   * The home index page.
   */
  import competitionService from '@/services/competition';


  export default {
    mounted() {
      competitionService.all(this.$route.params.comp_id);
    },
    components: {
      VLayout: require('@/layouts/default.vue'),
    },
  };
</script>
