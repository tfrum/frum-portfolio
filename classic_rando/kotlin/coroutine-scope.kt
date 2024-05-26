import kotlinx.coroutines.*

// Its been like 8 years since I worked in Kotlin, just wanted to remember how
// this scope worked
fun main() = runBlocking {
    // Launch a coroutine to perform a long-running math operation
    val deferred = async(Dispatchers.Default) {
        // Simulate a long-running computation
        var sum = 0
        for (i in 1..1_000_000) {
            sum += i
        }
        sum // Return the result
    }

    // Main thread keeps on keeping on
    println("Main thread is calculating...")
    val mainCalculation = (1..100).sum()
    println("Main thread calculated sum: $mainCalculation")

    // Wait for the coroutine to complete and get the result
    val result = deferred.await()
    println("Coroutine calculated sum: $result")
}
