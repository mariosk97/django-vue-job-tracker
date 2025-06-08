<template>
    <tr class="border-t">
        <td class="px-6 py-4">{{ job.company }}</td>
        <td class="px-6 py-4">{{ job.position }}</td>
        <td class="px-6 py-4">
        <span class="inline-block px-3 py-1 text-xs font-semibold bg-yellow-200 text-yellow-800 rounded-full">
            {{ job.status }}
        </span>
        </td>
        <td class="px-6 py-4">{{ job.date_applied }}</td>
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
</template>

<script>
export default {
  props: {
    job: Object
  }
}
</script>