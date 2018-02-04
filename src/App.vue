<template>
  <v-app id="app">
    <v-content>
      <v-container>
        <v-flex md6 offset-md3 justify-center>
          <risk-form-app/>
        </v-flex>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import RiskFormApp from '@/components/RiskFormApp'

export default {
  components: {RiskFormApp}
}
</script>

