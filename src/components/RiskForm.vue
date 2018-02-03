<template>
  <v-form v-model="valid">
    <div v-for="field in fields" :key="field.id">
      <v-text-field-field v-if="field.dataType === field.DATA_TYPES.TEXT"></v-text-field-field>
    </div>
  </v-form>
</template>

<script>
export default {
  data () {
    return {
      valid: true
    }
  },
  props: {
    fields: {
      type: Array,
      required: true
    }
  }
}
</script>

<style>

</style>
