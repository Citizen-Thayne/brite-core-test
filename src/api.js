import axios from 'axios'

const BASE_URL = 'api/risktypes/'

export default {

  async get (id = '') {
    const response = await axios.get(`${BASE_URL}${id}`)
    return response.data
  }
}
