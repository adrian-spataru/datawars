<template lang="pug">
#app
  .ui.container
    .ui.secondary.menu
      a.item Home
      a.item Description
      a.item Data
      a.active.item Leaderboard
      a.item Submit
      a.item Logout
  router-view.marginRoute
</template>

<script>
export default {
  name: 'app'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
