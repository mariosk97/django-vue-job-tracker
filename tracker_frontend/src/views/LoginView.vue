<template>
  <main class="min-h-screen flex items-center justify-center bg-gray-100 px-4">
    <div class="w-full max-w-md bg-white border border-gray-200 rounded-lg p-8 shadow-md">
      <form class="space-y-6" v-on:submit.prevent="submitForm()">
        <div>
          <label>E-mail</label><br>
          <input
            type="email"
            v-model="form.email"
            placeholder="Your e-mail address"
            class="w-full mt-2 py-3 px-4 border border-gray-200 rounded-lg"
          />
        </div>

        <div>
          <label>Password</label><br>
          <input
            type="password"
            v-model="form.password"
            placeholder="Your password"
            class="w-full mt-2 py-3 px-4 border border-gray-200 rounded-lg"
          />
        </div>

        <div class="text-center">
          <p class="font-medium">
            <RouterLink to="signup" class="underline text-purple-600">Don't have an account?</RouterLink>
          </p>
        </div>

        <template v-if="errors.length > 0">
          <div class="bg-red-300 text-white rounded-lg p-4">
            <p v-for="error in errors" :key="error">
              {{ error }}
            </p>
          </div>
        </template>

        <div>
          <button class="w-full py-3 px-4 bg-purple-600 text-white rounded-lg hover:bg-purple-700 transition">
            Log in
          </button>
        </div>
      </form>
    </div>
  </main>
</template>


<script>
import axios from 'axios'
import { useUserStore } from '@/stores/user'

export default {
  name: 'LoginView',

    setup() {
        const userStore = useUserStore()

        return {
            userStore
        }
    },

    data() {
        return {
            form: { //data entered by the user. Bound to data on form because of v-model.
                email: '',
                password: '',
            },
            
            errors: [],
        }
    },

    methods: {
        async submitForm() { //called when form is submitted because of v-on:submit
            this.errors = []

            //frondend (client-side) validation
            if (this.form.email === ''){
                this.errors.push('your email is missing')
            }

            if (this.form.password === ''){
                this.errors.push('your password is missing')
            }

            if (this.errors.length ===0) {
                await axios
                    .post ('/api/login/', this.form) //form data is sent to server
                    .then(response => { //server response. Login url returns a token
                        this.userStore.setToken(response.data) //saves token in the store
                        axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access
                    })
                    .catch(error => { //stops async function execution if error is caught
                        console.log('error', error)
                    })

                await axios
                    .get('/api/me/')    
                    .then(response => {
                        this.userStore.setUserInfo(response.data) //update user info in the store
                        this.$router.push('/') //redirect user to feed page
                    })  
                    .catch(error => {
                        console.log('error', error)
                    })  
            }
        }
    }
}
</script>