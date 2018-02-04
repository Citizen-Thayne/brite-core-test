<template>
  <v-text-field
    v-model="model"
    :label="name"
    :rules="rules"
    :counter="maxLength === Infinity ? false : maxLength"
  />
</template>

<script>
export default {
  props: {
    value: String,
    name: {
      type: String,
      required: true
    },
    minLength: {
      type: Number,
      default: 0
    },
    maxLength: {
      type: Number,
      default: Infinity
    }
  },
  computed: {
    rules () {
      return [
        (value = '') => this.minLength < length < this.maxLength
      ]
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
