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
                tr.positive
                td 1
                td
                    i.chevron.up.green.icon
                td.leaderName Awesome
                td 0.54321
                td 32
                td 3d
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
   * Leadboard Index Page
   * ============
   *
   * Page where the user can view the leaderboard
   */

  export default {
    components: {
      VLayout: require('@/layouts/default.vue'),
    },
  };
</script>
