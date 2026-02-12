import { useRef } from "react";
import { Link } from "react-router-dom";

function Login() {
    const emailRef = useRef();
    const passwordRef = useRef();

    function handleSubmit(event) {
        event.preventDefault();

        // Apenas visual por enquanto
        const data = {
            email: emailRef.current.value,
            password: passwordRef.current.value,
        };

        console.log("Dados de login (mock):", data);
        alert("Login visual (sem backend) ✔");
    }

    return (
        <main>
            <div className="flex justify-center px-4 sm:px-6 md:px-0 pt-10 sm:pt-16 md:pt-10 pb-10">
                <div className="bg-white w-full max-w-sm sm:max-w-md md:max-w-lg px-4 sm:px-6 md:px-10 py-5 sm:py-7 rounded-lg shadow-lg border border-gray-300">
                    <h2 className="text-2xl mb-5 font-semibold">Login</h2>

                    <form className="space-y-5 mb-8" onSubmit={handleSubmit}>
                        <div className="space-y-2">
                            <label htmlFor="email" className="text-base block font-semibold text-gray-800"> E-mail </label>
                            <input ref={emailRef} id="email" className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none" placeholder="E-mail" type="email"/>
                        </div>

                        <div className="space-y-2">
                            <label htmlFor="password" className="text-base block font-semibold text-gray-800"> Senha </label>
                            <input ref={passwordRef} id="password" className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none" placeholder="Senha" type="password" />
                        </div>

                        <div className="flex justify-center items-center">
                            <button type="submit" className="bg-[rgb(15,34,45)] text-white py-2 px-10 mt-4 rounded-md hover:bg-[#D9D9D9] hover:text-[rgb(15,34,45)] transition"> Fazer Login </button>
                        </div>
                    </form>

                    <Link to="/cadastro" className="flex justify-center text-blue-400 hover:underline"> Não possui uma conta? Cadastre-se </Link>
                </div>
            </div>
        </main>
    );
}

export default Login;
