<template> 
    <div v-if="isModalOpen" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
        <div class="bg-white p-6 rounded-lg w-full max-w-md shadow-lg">
            <h2 class="text-lg font-bold mb-4">Add New Job</h2>

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
    isModalOpen: Boolean
  },

  data() {
    return {
      form: {
        company: '',
        position: '',
        status: 'applied',
        date_applied: ''
      }
    }
  },

  methods: {
    submitForm() {

      //validate form

      axios.post('/api/jobs/create/', this.form)
        .then(response => {
          this.$emit('job-created')       // tell parent to reload jobs
          this.$emit('close')             // tell parent to close modal
          this.form = { company: '', position: '', status: 'applied', date_applied: '' }
        })
        .catch(error => console.log(error))
    },

    closeModal() {
    this.$emit('close') // Notify parent
  }
  }
}  

</script>  
   
