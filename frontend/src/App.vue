<template lang="pug">
#app
  .ui.container
    .ui.secondary.menu
      router-link(to="/").item Home
      a.item Description
      a.item Data
      a.active.item Leaderboard

      router-link(to="login", v-if="!isLoggedIn").item Login
      a(@click="logout", v-if="isLoggedIn").item Logout

  router-view.marginRoute
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'app',
  computed:{ ...mapGetters(["isLoggedIn", "errorLogin","test"]),},
  methods: {
    logout(event) {
      this.$store.dispatch("logout")

    }

  }



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
