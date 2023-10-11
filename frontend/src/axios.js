import axios from 'axios'

const instance = axios.create({
    baseURL: import.meta.env.API_HOST, // Use the API_HOST environment variable
})

export default instance
