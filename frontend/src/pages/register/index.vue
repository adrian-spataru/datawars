<template lang="pug">
v-layout
    .ui.two.column.centered.container.grid
        .center.aligned.column
            h2.ui.header Registration 
            form.ui.form
                .field(v-bind:class="{error: $store.state.auth.error}", @click="reseterror")
                    input(v-model="user.username", placeholder="username")
                .field(v-bind:class="{error: $store.state.auth.error}", @click="reseterror")
                    input(v-model="user.password", type="password" placeholder="password")
                p(v-if="$store.state.auth.error").ui.red Username taken or invalid input
                button.ui.fluid.button(v-on:click="register(user)") Register

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
      reseterror() {
        this.$store.dispatch('auth/reseterror');
      },
    },

    created() {
      this.reseterror();
    },

    components: {
      VLayout: require('@/layouts/default.vue'),

    },
  };
</script>
