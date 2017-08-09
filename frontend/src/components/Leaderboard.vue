<template lang="pug">
.Leaderboard
  .ui.container
    h1.ui.header Leaderboard
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
export default {
  name: 'Leaderboard',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>

<style scoped>
.leaderName {
  font-weight: 900;
}
</style>
