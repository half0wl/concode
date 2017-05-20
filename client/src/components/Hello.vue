<template>
  <div id="content" class="hello">
    <h1>{{ msg }}</h1>
    <p>
      <router-link class="link" to="/">{{ $t('buttons.home') }}</router-link>
    </p>
  </div>
</template>

<script>
export default {
  computed: {
    msg () {
      return this.$t('messages.hello', { name: this.name })
    },
    name () {
      const name = this.$route.params.name
      return name.charAt(0).toUpperCase() + name.slice(1)
    }
  }
}
</script>

<style lang="scss">
@import "./../styles/theme/variables";
h1 {
  color: $other;
}
</style>
