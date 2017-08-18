<template lang="pug">
v-layout
  h1.ui.header Registration
  .ui.input(v-bind:class="{error: $store.state.auth.error}")
    input(v-model="user.username", placeholder="username")
  br
  .ui.input(v-bind:class="{error: $store.state.auth.error}")
    input(v-model="user.password", type="password" placeholder="password")
  br
  button.ui.button(v-on:click="register(user)") Register
</template>

<script>
  /* ============
   * Register Index Page
   * ============
   *
   * Page where the user can register.
   */

  import authService from '@/services/auth';

  export default {

    data() {
      return {
        user: {
          username: null,
          password: null,
        },
      };
    },

    methods: {
      register(user) {
        console.log(user);
        authService.register(user);
      },
    },

    components: {
      VLayout: require('@/layouts/default.vue'),

    },
  };
</script>
