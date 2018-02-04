<template>
  <v-menu full-width>
      <v-text-field
        slot="activator"
        v-model="model"
        :label="name"
        readonly
      />
      <v-date-picker v-model="model" no-title scrollable actions>
          <template slot-scope="{ cancel }">
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn flat color="primary" @click="cancel">Cancel</v-btn>
            </v-card-actions>
          </template>
        </v-date-picker>
  </v-menu>
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
        ({length}) => this.minLength < length < this.maxLength
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
