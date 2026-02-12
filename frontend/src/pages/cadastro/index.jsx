import { useRef } from "react";
import { Link } from "react-router-dom";

function Cadastro() {
    const nameRef = useRef();
    const secondNameRef = useRef();
    const cpfRef = useRef();
    const birthDateRef = useRef();
    const emailRef = useRef();
    const passwordRef = useRef();

    function handleSubmit(event) {
        event.preventDefault();

        const data = {
            name: nameRef.current.value,
            secondName: secondNameRef.current.value,
            cpf: cpfRef.current.value,
            birthDate: birthDateRef.current.value,
            email: emailRef.current.value,
            password: passwordRef.current.value,
        };

        console.log("Dados do formulário (mock):", data);
        alert("Cadastro visual (sem backend) ✔");
    }

    return (
        <main>
            <div className="flex justify-center px-4 sm:px-6 md:px-0 pt-10 sm:pt-16 md:pt-10 pb-10">
                <div className="bg-white w-full max-w-sm sm:max-w-md md:max-w-lg px-4 sm:px-6 md:px-10 py-5 sm:py-7 rounded-lg shadow-lg border border-gray-300">

                    <h2 className="text-2xl mb-7 font-semibold text-center md:text-left">
                        Cadastrar
                    </h2>

                    <form className="space-y-5 mb-6" onSubmit={handleSubmit}>

                        <div className="space-y-2">
                            <label className="block font-semibold text-gray-800">Nome</label>
                            <input ref={nameRef} className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none" placeholder="Nome" />
                        </div>

                        <div className="space-y-2">
                            <label className="block font-semibold text-gray-800">Segundo Nome</label>
                            <input ref={secondNameRef} className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none" placeholder="Sobrenome" />
                        </div>

                        <div className="space-y-2">
                            <label className="block font-semibold text-gray-800">CPF</label>
                            <input ref={cpfRef} className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none" placeholder="CPF" />
                        </div>

                        <div className="space-y-2">
                            <label className="block font-semibold text-gray-800">Data de Nascimento</label>
                            <input ref={birthDateRef} type="date" className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none" />
                        </div>

                        <div className="space-y-2">
                            <label className="block font-semibold text-gray-800">E-mail</label>
                            <input ref={emailRef} type="email" className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none" placeholder="E-mail" />
                        </div>

                        <div className="space-y-2">
                            <label className="block font-semibold text-gray-800">Senha</label>
                            <input ref={passwordRef} type="password" className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none" placeholder="Senha" />
                        </div>

                        <div className="pt-2">
                            <button type="submit" className="w-full bg-[rgb(15,34,45)] text-white py-2 rounded-md hover:bg-[#D9D9D9] hover:text-[rgb(15,34,45)] transition">
                                Cadastrar-se
                            </button>
                        </div>
                    </form>

                    <Link to="/login" className="flex justify-center text-blue-400 hover:underline">
                        Já tem uma conta? Faça login
                    </Link>

                </div>
            </div>
        </main>
    );
}

export default Cadastro;
