<template lang="pug">
v-layout
    .ui.container(@click="reseterror")
        h1.ui.header Login
        .ui.input(v-bind:class="{error: $store.state.auth.error}")
            input(v-model="user.username", placeholder="username")
        br
        .ui.input(v-bind:class="{error: $store.state.auth.error}")
            input(v-model="user.password", type="password" placeholder="password")
        br
        p(v-if="$store.state.auth.error").ui.red Invalid Login Credentials
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
          error: false,
        },
      };
    },

    methods: {
      login(user) {
        authService.login(user);
      },
      reseterror() {
        this.$store.dispatch('auth/reseterror');
      },
    },

    components: {
      VLayout: require('@/layouts/default.vue'),
      VPanel: require('@/components/panel.vue'),
    },
  };
</script>
