<template>
  <v-select :items="items" v-model="model" :label="name" />
</template>

<script>
export default {
  props: {
    value: String,
    name: {
      type: String,
      required: true
    },
    values: {
      type: String,
      required: true
    }
  },
  computed: {
    items () {
      return this.values.split(',')
    },
    model: {
      get () {
        return this.value
      },
      set (newValue) {
        this.$emit('input', newValue)
      }
    }
  }
}
</script>

<style>

</style>
