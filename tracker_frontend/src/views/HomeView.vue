
<template>
  <JobModal
    :isModalOpen="isModalOpen"
    :jobToEdit="jobToEdit"
    @close="isModalOpen = false; jobToEdit = null"
    @job-created="getJobs"
    @job-updated="updateJob"
  />
  <main class="min-h-screen bg-gray-100 py-10 px-4">
    <div class="max-w-5xl mx-auto space-y-8">
      <!-- Header -->
      <div class="flex items-center justify-between">
        <h1 class="text-2xl font-bold text-gray-800">Welcome back, {{ userStore.user.name }}!</h1>
        <button 
          class="bg-red-500 text-white px-4 py-2 rounded-lg hover:bg-red-600 transition"
          @click="logout">
          Log out
        </button>
      </div>

      <!-- Actions -->
      <div class="flex flex-wrap items-center justify-between gap-4">
        <button @click="isModalOpen = true" class="bg-purple-600 text-white px-4 py-2 rounded-lg hover:bg-purple-700 transition">
          + Add New Job
        </button>

        <div class="flex gap-4">
          <select class="px-4 py-2 rounded-lg border border-gray-300 bg-white text-gray-700">
            <option value="">Filter by status</option>
            <option value="applied">Applied</option>
            <option value="interview">Interview</option>
            <option value="offer">Offer</option>
            <option value="rejected">Rejected</option>
          </select>

          <select class="px-4 py-2 rounded-lg border border-gray-300 bg-white text-gray-700">
            <option value="">Sort by</option>
            <option value="date_desc">Newest first</option>
            <option value="date_asc">Oldest first</option>
            <option value="company">Company name</option>
          </select>
        </div>
      </div>

      <!-- Job Table -->
      <div class="overflow-x-auto bg-white border border-gray-200 rounded-lg shadow">
        <table class="min-w-full table-auto text-left text-sm">
          <thead class="bg-gray-50 border-b">
            <tr>
              <th class="px-6 py-4 font-medium text-gray-700">Company</th>
              <th class="px-6 py-4 font-medium text-gray-700">Position</th>
              <th class="px-6 py-4 font-medium text-gray-700">Status</th>
              <th class="px-6 py-4 font-medium text-gray-700">Date Applied</th>
              <th class="px-6 py-4 font-medium text-gray-700">Actions</th>
            </tr>
          </thead>
          <tbody>

            <JobItem
              v-for="job in jobs"
              :key="job.id"
              :job="job"
              @delete-job="deleteJob"
              @edit-job="editJob"
            />

            <tr v-if="jobs.length === 0">
              <td colspan="5" class="text-center py-6 text-gray-500">
                You haven’t added any jobs yet.
              </td>
            </tr>

          </tbody>
        </table>
      </div>
    </div>
  </main>
</template>

<script>

import axios from 'axios'
import { useUserStore } from '@/stores/user'
import JobModal from '@/components/JobModal.vue'
import JobItem from '@/components/JobItem.vue';

export default {
  name: 'HomeView',

  components: { 
    JobModal,
    JobItem,
   },

    setup() {
      const userStore = useUserStore()
      
      return {
          userStore,
          
      }
  }, 

  data() {
    return {
      jobs: [],
      user: {},
      isModalOpen: false,
      jobToEdit: null,
    }
  },

      mounted() { //Calls the getFeed method after the component is mounted to load the jobs
          if (!this.userStore.user.isAuthenticated) {
            this.$router.push('/login')
          }
          
        this.getJobs()
    },

  methods: {
    logout() {
        console.log("logout")
        this.userStore.removeToken()
        this.$router.push('/login')
    },
    
    getJobs() {
      axios
        .get('/api/jobs/')
        .then(response => {
          console.log('data', response.data)
          this.jobs = response.data
        })    
        .catch(error => {
          console.log('error', error)
        })
    },
    
    deleteJob(id) {
      axios
        .delete(`/api/jobs/delete/${id}/`)
        .then(response => {
          console.log("job deleted")
          this.jobs = this.jobs.filter(job => job.id !== id)
          //this.toastStore.showToast(3000, 'Job deleted successfully', 'bg-emerald-500')
        })    
        .catch(error => {
          console.log('error', error)
        })
    },

    editJob(job) {
      console.log('Edit job:', job)
      this.jobToEdit = job
      this.isModalOpen = true
    },

    updateJob(updatedJob) {
      const index = this.jobs.findIndex(job => job.id === updatedJob.id)
      if (index !== -1) this.jobs.splice(index, 1, updatedJob)
    }


  }  
} 

</script>
