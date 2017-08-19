<template lang="pug">
v-layout
    h1.ui.header(v-text="$store.state.competition.name") 
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
