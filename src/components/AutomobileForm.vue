<template>
  <div class="automobile-form">
    <h1>New Automobile Risk</h1>
    <risk-form v-if="ready" :fields="riskType.fields">
    </risk-form>
    {{riskType}}
  </div>
</template>

<script>
import RiskForm from '@/components/RiskForm'
import riskTypes from '@/api'

export default {
  components: { RiskForm },
  data () {
    return {
      ready: false,
      riskType: null
    }
  },
  async mounted () {
    this.riskType = await riskTypes.get(1)
    this.ready = true
  }
}
</script>

<style>

</style>
