<template lang="pug">
v-layout
    .ui.container
        table.ui.table
            thead.headerTable
                tr
                th.one.wide #
                th.one.wide Trend
                th.nine.wide Team
                th.two.wide Score
                th.one.wide Entries
                th.one.wide Last
            tbody
                tr(v-for="item in $store.state.leaderboard.public").positive
                    td 1
                    td
                        i.chevron.up.green.icon
                    td(v-text="item.team_name").leaderName
                    td(v-text="item.public_score")
                    td 32
                    td 3d
                //-
                    tr
                    td 2
                    td
                        i.chevron.down.red.icon
                    td.leaderName Blue
                    td 0.53211
                    td 3
                    td 2h   
                    tr
                    td 2
                    td
                        i.minus.gray.icon
                    td.leaderName Blue
                    td 0.53211
                    td 3
                    td 2h
                    tr
                    td 2
                    td
                        i.chevron.down.red.icon
                    td.leaderName Blue
                    td 0.53211
                    td 3
                    td 2h 
</template>

<script>
  /* ============
   * Leaderboard Page
   * ============
   *
   * The leaderboard of a competition page.
   */
  import leaderboardServices from '@/services/leaderboard';


  export default {
    mounted() {
      leaderboardServices.publicLeaderboard(this.$route.params.comp_id);
    },
    components: {
      VLayout: require('@/layouts/default.vue'),
    },
  };
</script>
