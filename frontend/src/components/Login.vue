<template lang="pug">
.Login
  .ui.container
    h1.ui.header Login
    .ui.input(v-bind:class="{error: test}")
      input(type="text" placeholder="Username", v-model="username")
    
    .ui.input
      input(type="text" placeholder="Password", v-model="password")
    button.ui.button(v-on:click="submit") Login


    
</template>

<script>
import { mapGetters, mapActions } from 'vuex'


export default {
  
  name: 'Login',
  data () {
    return {
      username: "",
      password: "",
     
    }
  },
  computed:{ ...mapGetters(["isLoggedIn", "errorLogin","test"]),},

  methods: {
    submit (event) {
      console.log("Logging "+this.username+"...")
      this.$store.commit("LOGIN_FAIL")
       this.$store.dispatch("login", {
        username: this.username,
        password: this.password
      }).then(res => {
        
      })

    }
  }
}
</script>

<style scoped>
.leaderName {
  font-weight: 900;
}
</style>
