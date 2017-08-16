<template lang="pug">
.Login
  .ui.container
    h1.ui.header Login
    .ui.input
      input(type="text" placeholder="Username", v-model="username")
    
    .ui.input
      input(type="text" placeholder="Password", v-model="password")
    button.ui.button(v-on:click="submit") Login


    
</template>

<script>

export default {
  
  name: 'Login',
  data () {
    return {
      username: "",
      password: "",
     
    }
  },
  methods: {
    submit (event) {
      console.log("Logging "+this.username+"...")

    }
  }
}
</script>

<style scoped>
.leaderName {
  font-weight: 900;
}
</style>
