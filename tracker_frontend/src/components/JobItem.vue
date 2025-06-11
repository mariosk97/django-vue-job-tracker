<template>
    <tr class="border-t">
        <td class="px-6 py-4">{{ job.company }}</td>
        <td class="px-6 py-4">{{ job.position }}</td>
        <td class="px-6 py-4">
        <span 
            class="inline-block px-3 py-1 text-xs font-semibold rounded-full"
            :class="{
                'bg-yellow-200 text-yellow-800': job.status === 'applied',
                'bg-blue-200 text-blue-800': job.status === 'interview',
                'bg-green-200 text-green-800': job.status === 'offer',
                'bg-red-200 text-red-800': job.status === 'rejected',
            }"
            >
            {{ job.status.charAt(0).toUpperCase() + job.status.slice(1) }}
        </span>
        </td>
        <td class="px-6 py-4">{{ job.date_applied }}</td>
        <td class="px-6 py-4">
        <div class="flex space-x-4">
            <!-- Edit Icon -->
            <button @click="handleEdit" class="text-gray-500 hover:text-blue-600 transition">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5M18.5 2.5l2.5 2.5L13 13H10v-3l8.5-8.5z" />
            </svg>
            </button>

            <!-- Delete Icon (placeholder for now) -->
            <button @click="showConfirm = true" class="text-gray-500 hover:text-red-600 transition">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6M9 7h6m2 0H7" />
            </svg>
            </button>

            <div v-if="showConfirm" class="fixed inset-0 bg-black bg-opacity-40 flex items-center justify-center z-50">
              <div class="bg-white p-4 rounded-lg shadow w-80">
                <p class="text-gray-800 mb-4">Are you sure you want to delete this job?</p>
                <div class="flex justify-end gap-2">
                  <button @click="showConfirm = false" class="px-4 py-2 bg-gray-300 rounded">Cancel</button>
                  <button @click="handleDelete" class="px-4 py-2 bg-red-600 text-white rounded hover:bg-red-700">Delete</button>
                </div>
              </div>
            </div>
        </div>
        </td>
    </tr>
</template>

<script>
export default {
  props: {
    job: Object
  },

  data() {
    return {
      showConfirm: false
    }
  },

  methods: {
  handleDelete() {
    this.$emit('delete-job', this.job.id)
    this.showConfirm = false
    console.log(this.job)
    },
    
    handleEdit() {
      this.$emit('edit-job', this.job)
    }
  },
}
</script>