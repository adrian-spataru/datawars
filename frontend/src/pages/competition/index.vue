<template lang="pug">
v-layout
    h1.ui.header Competitons
    ul.ui.relaxed.list
        .item(v-for="competition in $store.state.competition.competitions")
            i.large.star.middle.aligned.icon
            .content
                a.header(v-text="competition.name")
                .description(v-text="competition.ending_at")
</template>
<script>
  /* ============
   * Home Index Page
   * ============
   *
   * The home index page.
   */
  import competitionsService from '@/services/competitions';


  export default {
    mounted() {
      competitionsService.all();
    },
    components: {
      VLayout: require('@/layouts/default.vue'),
    },
  };
</script>
