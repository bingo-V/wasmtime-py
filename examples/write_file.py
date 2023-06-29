from wasmtime import Store, Module, Engine, Linker, WasiConfig

engine = Engine()
module = Module.from_file(engine, "examples/write_file.wasm")
linker = Linker(engine)
linker.define_wasi()
store = Store(engine)

wasi_config = WasiConfig()
wasi_config.preopen_dir('.', '.')
wasi_config.inherit_stdout()
store.set_wasi(wasi_config)

instance = linker.instantiate(store, module)
run = instance.exports(store)["_start"]
run(store)