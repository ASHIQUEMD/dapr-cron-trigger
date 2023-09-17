# dapr-cron-trigger

## Error

`== APP == [2023-09-17T04:00:00.021Z] Worker process started and initialized.
== APP == [2023-09-17T04:00:08.035Z] Executing 'Functions.dbt' (Reason='(null)', Id=d7ec3eda-13eb-4079-a66a-7fece15016d5)
== APP == [2023-09-17T04:00:08.088Z] Executed 'Functions.dbt' (Failed, Id=d7ec3eda-13eb-4079-a66a-7fece15016d5, Duration=68ms)
== APP == [2023-09-17T04:00:08.088Z] System.Private.CoreLib: Exception while executing function: Functions.dbt. System.Private.CoreLib: Result: Failure
== APP == Exception: AttributeError: 'NoneType' object has no attribute 'type'
== APP == Stack:   File "C:\Program Files\Microsoft\Azure Functions Core Tools\workers\python\3.11\WINDOWS\X64\azure_functions_worker\dispatcher.py", line 456, in _handle__invocation_request
== APP ==     args[pb.name] = bindings.from_incoming_proto(
== APP ==                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
== APP ==   File "C:\Program Files\Microsoft\Azure Functions Core Tools\workers\python\3.11\WINDOWS\X64\azure_functions_worker\bindings\meta.py", line 90, in from_incoming_proto
== APP ==     return binding.decode(datum, trigger_metadata=metadata)
== APP ==            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
== APP ==   File "C:\Program Files\Microsoft\Azure Functions Core Tools\workers\python\3.11\WINDOWS\X64\azure_functions_worker\bindings\generic.py", line 37, in decode
== APP ==     data_type = data.type
== APP ==                 ^^^^^^^^^
== APP == .
== APP == [2023-09-17T04:00:08.105Z] Function invocation failed.
== APP == [2023-09-17T04:00:08.105Z] System.Private.CoreLib: Exception while executing function: Functions.dbt. System.Private.CoreLib: Result: Failure
== APP == Exception: AttributeError: 'NoneType' object has no attribute 'type'
== APP == Stack:   File "C:\Program Files\Microsoft\Azure Functions Core Tools\workers\python\3.11\WINDOWS\X64\azure_functions_worker\dispatcher.py", line 456, in _handle__invocation_request
== APP ==     args[pb.name] = bindings.from_incoming_proto(
== APP ==                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
== APP ==   File "C:\Program Files\Microsoft\Azure Functions Core Tools\workers\python\3.11\WINDOWS\X64\azure_functions_worker\bindings\meta.py", line 90, in from_incoming_proto
== APP ==     return binding.decode(datum, trigger_metadata=metadata)
== APP ==            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
== APP ==   File "C:\Program Files\Microsoft\Azure Functions Core Tools\workers\python\3.11\WINDOWS\X64\azure_functions_worker\bindings\generic.py", line 37, in decode
== APP ==     data_type = data.type
== APP ==                 ^^^^^^^^^
== APP == .
== APP == [2023-09-17T04:00:18.002Z] Executing 'Functions.dbt' (Reason='(null)', Id=00b1a9d2-9fcc-40e7-8bb7-98fe0837a458)
== APP == [2023-09-17T04:00:18.004Z] Executed 'Functions.dbt' (Failed, Id=00b1a9d2-9fcc-40e7-8bb7-98fe0837a458, Duration=2ms)   
== APP == [2023-09-17T04:00:18.004Z] System.Private.CoreLib: Exception while executing function: Functions.dbt. System.Private.CoreLib: Result: Failure
== APP == Exception: AttributeError: 'NoneType' object has no attribute 'type'
== APP == Stack:   File "C:\Program Files\Microsoft\Azure Functions Core Tools\workers\python\3.11\WINDOWS\X64\azure_functions_worker\dispatcher.py", line 456, in _handle__invocation_request
== APP ==     args[pb.name] = bindings.from_incoming_proto(
== APP ==                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
== APP ==   File "C:\Program Files\Microsoft\Azure Functions Core Tools\workers\python\3.11\WINDOWS\X64\azure_functions_worker\bindings\meta.py", line 90, in from_incoming_proto
== APP ==     return binding.decode(datum, trigger_metadata=metadata)
== APP ==            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
== APP ==   File "C:\Program Files\Microsoft\Azure Functions Core Tools\workers\python\3.11\WINDOWS\X64\azure_functions_worker\bindings\generic.py", line 37, in decode
== APP ==     data_type = data.type
== APP ==                 ^^^^^^^^^
== APP == .
== APP == [2023-09-17T04:00:18.005Z] Function invocation failed.
== APP == [2023-09-17T04:00:18.006Z] System.Private.CoreLib: Exception while executing function: Functions.dbt. System.Private.CoreLib: Result: Failure
== APP == Exception: AttributeError: 'NoneType' object has no attribute 'type'
== APP == Stack:   File "C:\Program Files\Microsoft\Azure Functions Core Tools\workers\python\3.11\WINDOWS\X64\azure_functions_worker\dispatcher.py", line 456, in _handle__invocation_request
== APP ==     args[pb.name] = bindings.from_incoming_proto(
== APP ==                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
== APP ==   File "C:\Program Files\Microsoft\Azure Functions Core Tools\workers\python\3.11\WINDOWS\X64\azure_functions_worker\bindings\meta.py", line 90, in from_incoming_proto
== APP ==     return binding.decode(datum, trigger_metadata=metadata)
== APP ==            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
== APP ==   File "C:\Program Files\Microsoft\Azure Functions Core Tools\workers\python\3.11\WINDOWS\X64\azure_functions_worker\bindings\generic.py", line 37, in decode
== APP ==     data_type = data.type
== APP ==                 ^^^^^^^^^
== APP == .`