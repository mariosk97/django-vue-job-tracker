<template>
  <main class="min-h-screen bg-gray-100 py-10 px-4">
    <div class="max-w-5xl mx-auto space-y-8">
      <!-- Header -->
      <div class="flex items-center justify-between">
        <h1 class="text-2xl font-bold text-gray-800">Welcome back, {{ userName }}!</h1>
        <button class="bg-red-500 text-white px-4 py-2 rounded-lg hover:bg-red-600 transition">
          Log out
        </button>
      </div>

      <!-- Actions -->
      <div class="flex flex-wrap items-center justify-between gap-4">
        <button class="bg-purple-600 text-white px-4 py-2 rounded-lg hover:bg-purple-700 transition">
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
            <!-- Example row -->
            <tr class="border-t">
              <td class="px-6 py-4">Stripe</td>
              <td class="px-6 py-4">Backend Developer</td>
              <td class="px-6 py-4">
                <span class="inline-block px-3 py-1 text-xs font-semibold bg-yellow-200 text-yellow-800 rounded-full">
                  Applied
                </span>
              </td>
              <td class="px-6 py-4">May 24, 2025</td>
              <td class="px-6 py-4">
                <div class="flex space-x-4">
                  <!-- Edit Icon -->
                  <button class="text-gray-500 hover:text-blue-600 transition">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5M18.5 2.5l2.5 2.5L13 13H10v-3l8.5-8.5z" />
                    </svg>
                  </button>

                  <!-- Delete Icon (placeholder for now) -->
                  <button class="text-gray-500 hover:text-red-600 transition">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6M9 7h6m2 0H7" />
                    </svg>
                  </button>
                </div>
              </td>
            </tr>
            <!-- Add more rows here dynamically -->
          </tbody>
        </table>
      </div>
    </div>
  </main>
</template>

<script setup>

</script>

