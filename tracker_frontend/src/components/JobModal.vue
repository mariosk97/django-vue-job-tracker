<template> 
    <div v-if="isModalOpen" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
        <div class="bg-white p-6 rounded-lg w-full max-w-md shadow-lg">
            <h2 class="text-lg font-bold mb-4">
              {{ jobToEdit ? 'Edit Job' : 'Add New Job' }}
            </h2>

            <form class="space-y-4">
                <input type="text" v-model="form.company" placeholder="Company" class="w-full border px-4 py-2 rounded" />
                <input v-model="form.position" placeholder="Position" class="w-full border px-4 py-2 rounded" />
                <select v-model="form.status" class="w-full border px-4 py-2 rounded">
                    <option value="applied">Applied</option>
                    <option value="interview">Interview</option>
                    <option value="offer">Offer</option>
                    <option value="rejected">Rejected</option>
                </select>
                <input type="date" v-model="form.date_applied" class="w-full border px-4 py-2 rounded" />
            </form>

            <template v-if="errors.length > 0">
              <div class="bg-red-300 text-white rounded-lg p-6">
                <p v-for="error in errors" v-bind:key="error">
                  {{ error }}
                </p>
              </div>
            </template>

            <div class="mt-6 flex justify-end gap-2">
                <button @click="closeModal" class="px-4 py-2 bg-gray-300 rounded">Cancel</button>
                <button @click="submitForm" class="px-4 py-2 bg-purple-600 text-white rounded hover:bg-purple-700">
                  Add Job
                </button>
            </div>    
        </div>
    </div>   
</template>    

<script>
import axios from 'axios'

export default {
  props: {
    isModalOpen: Boolean,
    jobToEdit: Object,
  },

  data() {
    return {
      form: {
        company: '',
        position: '',
        status: 'applied',
        date_applied: ''
      },
      errors: [],
    }
  },

  watch: {
    jobToEdit: {
      immediate: true,
      handler(newJob) {
        if (newJob) {
          this.form = {
            company: newJob.company,
            position: newJob.position,
            status: newJob.status,
            date_applied: newJob.date_applied
          }
        } else {
          this.form = {
            company: '',
            position: '',
            status: 'applied',
            date_applied: ''
          }
        }
      }
    }
  },

  methods: {
    submitForm() {
      this.errors = []

      if (this.form.company === '') this.errors.push('company is missing')
      if (this.form.position === '') this.errors.push('position is missing')
      if (this.form.date_applied === '') this.errors.push('date applied is missing')

      if (this.errors.length === 0) {
        if (this.jobToEdit) {
          axios.put(`/api/jobs/update/${this.jobToEdit.id}/`, this.form)
            .then(response => {
              this.$emit('job-updated', response.data)
              this.$emit('close')
            })
            .catch(error => console.log(error))
        } else {
          axios.post('/api/jobs/create/', this.form)
            .then(response => {
              this.$emit('job-created', response.data)
              this.$emit('close')
            })
            .catch(error => console.log(error))
        }
      }
    },

    closeModal() {
      this.$emit('close')
    }
  }
}
</script>

   
