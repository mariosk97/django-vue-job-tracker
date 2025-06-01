<template>
  <main class="min-h-screen flex items-center justify-center bg-gray-100 px-4">
    <div class="w-full max-w-md bg-white border border-gray-200 rounded-lg p-8 shadow-md">
      <form class="space-y-6" v-on:submit.prevent="submitForm()">
        <div>
          <label>Name</label><br>
          <input type="text" v-model="form.name" placeholder="Your full name" class="w-full mt-2 py-3 px-4 border border-gray-200 rounded-lg">
        </div>

        <div>
          <label>E-mail</label><br>
          <input type="email" v-model="form.email" placeholder="Your e-mail address" class="w-full mt-2 py-3 px-4 border border-gray-200 rounded-lg">
        </div>

        <div>
          <label>Password</label><br>
          <input type="password" v-model="form.password1" placeholder="Your password" class="w-full mt-2 py-3 px-4 border border-gray-200 rounded-lg">
        </div>

        <div>
          <label>Repeat password</label><br>
          <input type="password" v-model="form.password2" placeholder="Repeat your password" class="w-full mt-2 py-3 px-4 border border-gray-200 rounded-lg">
        </div>

        <div>
          <button class="w-full py-3 px-4 bg-purple-600 text-white rounded-lg hover:bg-purple-700 transition">Sign Up</button>
        </div>

        <div class="text-center">
          <p class="font-medium">
            <RouterLink to="login" class="underline text-purple-600">Already have an account?</RouterLink>
          </p>
        </div>

        <template v-if="errors.length > 0">
          <div class="bg-red-300 text-white rounded-lg p-4">
            <p v-for="error in errors" :key="error">
              {{ error }}
            </p>
          </div>
        </template>
      </form>
    </div>
  </main>
</template>


<script>
import axios from 'axios'
import { useToastStore } from '@/stores/toast'

export default {
  data() {
    return {
      toastStore: null,
      form: {
        email: '',
        name: '',
        password1: '',
        password2: '',
      },
      errors: [],
    }
  },

  mounted() {
    this.toastStore = useToastStore()
  },

  methods: {
    submitForm() {
      if (!this.toastStore) {
        console.error('Toast store not initialized yet')
        return
      }

      this.errors = []

      if (this.form.email === '') this.errors.push('your email is missing')
      if (this.form.name === '') this.errors.push('your name is missing')
      if (this.form.password1 === '') this.errors.push('your password is missing')
      if (this.form.password1 !== this.form.password2) this.errors.push('your passwords do not match')

      if (this.errors.length === 0) {
        axios.post('/api/signup/', this.form)
          .then(response => {
            if (response.data.message === 'success') {
              this.toastStore.showToast(5000, 'The user is registered. Please log in', 'bg-emerald-500')
              this.form.email = ''
              this.form.name = ''
              this.form.password1 = ''
              this.form.password2 = ''
            } else {
              this.toastStore.showToast(5000, 'Something went wrong. Please try again', 'bg-red-300')
            }
          })
          .catch(error => {
            console.log('error', error)
          })
      }
    }
  }
}

</script>