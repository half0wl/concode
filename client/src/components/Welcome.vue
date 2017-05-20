<template>
  <div id="content">
    <p>
      {{ $t('messages.welcome') }}
    </p>
    <p>
      <router-link class="link" to="/hello/concode">{{ $t('buttons.hello') }}</router-link>
    </p>
  </div>
</template>

<script>
export default {}
</script>

<style lang="scss">
</style>
