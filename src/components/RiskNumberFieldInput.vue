<template>
  <v-text-field v-model="model" :label="name" :rules="rules" />
</template>

<script>
export default {
  props: {
    value: Number,
    name: {
      type: String,
      required: true
    },
    minValue: {
      type: Number,
      default: -Infinity
    },
    maxValue: {
      type: Number,
      default: Infinity
    }
  },
  computed: {
    rules () {
      let self = this
      return [
        function (value) {
          return isNaN(value) ? 'Numbers only' : true
        },
        function (value) {
          return self.minValue <= value && value <= self.maxValue ? true : `Number must be between ${self.minValue} and ${self.maxValue}`
        }
      ]
    },
    model: {
      get () {
        return this.value
      },
      set (newValue) {
        this.$emit('input', parseFloat(newValue) || null)
      }
    }
  }
}
</script>

<style>

</style>
