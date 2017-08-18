<template lang="pug">
v-layout
    .ui.container
        h1.ui.header Login
        .ui.input
            input(v-model="user.username", placeholder="username")
        br
        .ui.input
            input(v-model="user.password", type="password" placeholder="password")
        br
        button.ui.button(v-on:click="login(user)") Login
        br
        p No account?
        router-link(:to="{name: 'register.index'}") Register 
</template>

<script>
  /* ============
   * Login Index Page
   * ============
   *
   * Page where the user can login.
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
      login(user) {
        authService.login(user);
      },
    },

    components: {
      VLayout: require('@/layouts/default.vue'),
      VPanel: require('@/components/panel.vue'),
    },
  };
</script>
