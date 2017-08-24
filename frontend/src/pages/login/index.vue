<template lang="pug">
v-layout
    .ui.five.column.centered.grid
        .center.aligned.column
            h2.ui.header Login
            form.ui.form
                .field(v-bind:class="{error: $store.state.auth.error}", @click="reseterror")
                    input(v-model="user.username", placeholder="username")
                .field(v-bind:class="{error: $store.state.auth.error}", @click="reseterror")
                    input(v-model="user.password", type="password" placeholder="password")
                p(v-if="$store.state.auth.error").ui.red Invalid Login Credentials
                button.ui.fluid.button(v-on:click="login(user)") Login
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
