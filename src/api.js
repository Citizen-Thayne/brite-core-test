import axios from 'axios'

import {
  RiskType
} from '@/models'

const BASE_URL = '/api/risktypes/'

export default {
  async get (id) {
    const response = await axios.get(`${BASE_URL}${id}`)
    let riskType = new RiskType(response.data)
    return riskType
  }
}
