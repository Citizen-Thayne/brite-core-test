<template>
  <div class="risk-form-app">
    <v-card>
      <v-toolbar>
         <v-menu class="risk-type-select-menu">
          <v-toolbar-side-icon slot="activator"></v-toolbar-side-icon>
          <v-list>
            <v-list-tile 
              v-for="riskType in riskTypes" 
              :key="riskType.id" 
              @click="selectRiskType(riskType)">
                {{riskType.name}}
              </v-list-tile>
          </v-list>
        </v-menu>
        <v-toolbar-title>{{currentRiskType ? currentRiskType.name : 'Select Risk Type'}}</v-toolbar-title>
      </v-toolbar>
      <v-card-text>
        <v-list v-if="!currentRiskType">
          <v-list-tile v-for="riskType in riskTypes" :key="riskType.id" @click="selectRiskType(riskType)">
            <v-list-tile-content>{{riskType.name}}</v-list-tile-content>
          </v-list-tile>
        </v-list>
        <risk-form v-else v-bind="currentRiskType" :key="currentRiskType.id" />
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
import riskTypes from '@/api'
import RiskForm from '@/components/RiskForm'

export default {
  components: {
    RiskForm
  },
  data: () => ({
    riskTypes: [],
    currentRiskType: null
  }),
  methods: {
    selectRiskType (riskType) {
      this.currentRiskType = riskType
    }
  },
  async created () {
    this.riskTypes = await riskTypes.get()
  }
}
</script>

<style>

</style>

