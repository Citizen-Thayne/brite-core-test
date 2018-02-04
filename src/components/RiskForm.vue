<template>
  <v-form v-model="valid">
    <div v-for="field in fields" :key="field.id">
      <component :is="getInputComponent(field.dataType)" v-bind="field" v-model="formModel[field.id]" />
    </div>
    <h4>Form Model:</h4>
    <div>{{formModel}}</div>
  </v-form>
</template>

<script>
import RiskTextFieldInput from '@/components/RiskTextFieldInput'
import RiskNumberFieldInput from '@/components/RiskNumberFieldInput'
import RiskEnumFieldInput from '@/components/RiskEnumFieldInput'
import RiskDateFieldInput from '@/components/RiskDateFieldInput'

export default {
  data () {
    return {
      valid: true,
      formModel: {}
    }
  },
  props: {
    name: {
      type: String,
      required: true
    },
    fields: {
      type: Array,
      required: true
    }
  },
  methods: {
    getInputComponent (dataType) {
      return {
        'text': RiskTextFieldInput,
        'number': RiskNumberFieldInput,
        'enum': RiskEnumFieldInput,
        'date': RiskDateFieldInput
      }[dataType]
    }
  }
}
</script>

<style>

</style>
