import errno
import gc
import operator
import sys
from unittest import skipIf
    fcntl = None  # type: ignore[assignment]
try:
    from twisted.internet import process as _process
    from twisted.internet.process import ProcessReader, ProcessWriter, PTYProcess
except ImportError:
    process = None
    ProcessReader = object  # type: ignore[misc,assignment]
    ProcessWriter = object  # type: ignore[misc,assignment]
    PTYProcess = object  # type: ignore[misc,assignment]
else:
    process = _process
from zope.interface.verify import verifyObject

from twisted.internet import defer, error, interfaces, protocol, reactor
from twisted.python import procutils, runtime
from twisted.python.compat import networkString
from twisted.python.filepath import FilePath
pyExe = FilePath(sys.executable).path
properEnv = dict(os.environ)
properEnv["PYTHONPATH"] = os.pathsep.join(sys.path)







        self.data = b""
        self.err = b""
                raise RuntimeError(f"Data was {self.data!r} instead of 'abcd'")
                raise RuntimeError(f"Err was {self.err!r} instead of '1234'")
        if self.buffer[self.count : self.count + len(data)] != data:
        msg(f"Received {data!r} from child stdout")
        msg(f"Received {data!r} from child stderr")
        msg(f"Child exited: {reason.getTraceback()!r}")
            return self.deferred.errback(ValueError(f"wrong termination: {reason}"))
            signalValue = getattr(signal, "SIG" + self.signal)
                ValueError(f"SIG{self.signal}: exitCode is {v.exitCode}, not None")
            )
                ValueError(
                    "SIG%s: .signal was %s, wanted %s"
                    % (self.signal, v.signal, signalValue)
                )
            )
                ValueError(f"SIG{self.signal}: {os.WTERMSIG(v.status)}")
            )

    programName: bytes = b""
            self, pyExe, [pyExe, "-u", "-m", self.programName] + argv, env=env
        )

        return b"".join(chunks).split(b"\0")

        environBytes = b"".join(chunks)
        if not environBytes:
        environb = iter(environBytes.split(b"\0"))
                k = next(environb)
                v = next(environb)
@skipIf(
    not interfaces.IReactorProcess(reactor, None),
    "reactor doesn't support IReactorProcess",
)

        scriptPath = "twisted.test.process_twisted"
        reactor.spawnProcess(
            p,
            pyExe,
            [pyExe, "-u", "-m", scriptPath],
            env=properEnv,
            path=None,
            usePTY=self.usePTY,
        )
            self.assertEqual(
                p.outF.getvalue(),
                b"hello, worldabc123",
                "Output follows:\n"
                "%s\n"
                "Error message from process_twisted follows:\n"
                "%s\n" % (p.outF.getvalue(), p.errF.getvalue()),
            )

    def test_patchSysStdoutWithNone(self):
        """
        In some scenarious, such as Python running as part of a Windows
        Windows GUI Application with no console, L{sys.stdout} is L{None}.
        """
        import sys

        self.patch(sys, "stdout", None)
        return self.test_stdio()

    def test_patchSysStdoutWithStringIO(self):
        """
        Some projects which use the Twisted reactor
        such as Buildbot patch L{sys.stdout} with L{io.StringIO}
        before running their tests.
        """
        import sys
        from io import StringIO

        stdoutStringIO = StringIO()
        self.patch(sys, "stdout", stdoutStringIO)
        return self.test_stdio()

    def test_patch_sys__stdout__WithStringIO(self):
        """
        If L{sys.stdout} and L{sys.__stdout__} are patched with L{io.StringIO},
        we should get a L{ValueError}.
        """
        import sys
        from io import StringIO

        self.patch(sys, "stdout", StringIO())
        self.patch(sys, "__stdout__", StringIO())
        return self.test_stdio()
        procTrans = reactor.spawnProcess(
            p, pyExe, [pyExe, b"-u", b"-m", scriptPath], env=properEnv
        )
    @skipIf(
        os.environ.get("CI", "").lower() == "true"
        and runtime.platform.getType() == "win32"
        and sys.version_info[0:2] in [(3, 7), (3, 8), (3, 9)],
        "See https://twistedmatrix.com/trac/ticket/10014",
    )
        reactor.spawnProcess(p, pyExe, [pyExe, b"-u", b"-m", scriptPath], env=properEnv)

                error.ProcessExitedAlready, p.transport.signalProcess, "INT"
            )
                import glob

                import process_tester  # type: ignore[import]

            except BaseException:

    @skipIf(
        os.environ.get("CI", "").lower() == "true"
        and runtime.platform.getType() == "win32"
        and sys.version_info[0:2] in [(3, 7), (3, 8), (3, 9)],
        "See https://twistedmatrix.com/trac/ticket/10014",
    )
                self.assertEqual(
                    p.stages,
                    [1, 2, 3, 4, 5],
                    "[%d] stages = %s" % (id(p.transport), str(p.stages)),
                )
        args = [pyExe, b"-u", b"-m", scriptPath]
        reactor.spawnProcess(p, pyExe, [pyExe, b"-u", b"-m", scriptPath], env=properEnv)
            self.assertTrue(hasattr(p, "buffer"))
        args = [
            br"a\"b ",
            br"a\b ",
            br' a\\"b',
            br" a\\b",
            br'"foo bar" "',
            b"\tab",
            b'"\\',
            b'a"b',
            b"a'b",
        ]
        reactor.spawnProcess(
            p, pyExe, [pyExe, b"-u", b"-m", scriptPath] + args, env=properEnv, path=None
        )
        return d.addCallback(processEnded)

        for num in (0, 1):
            p = reactor.spawnProcess(
                self.pp[num],
                pyExe,
                [pyExe, b"-u", b"-m", scriptPath],
                env=properEnv,
                usePTY=usePTY,
            )
        if self.verbose:
            print("closing stdin [%d]" % num)
        if self.verbose:
            print(self.pp[0].finished, self.pp[1].finished)
        return defer.gatherResults([p.deferred for p in self.pp])
        if self.verbose:
            print("starting processes")
@skipIf(runtime.platform.getType() != "win32", "Only runs on Windows")
@skipIf(
    not interfaces.IReactorProcess(reactor, None),
    "reactor doesn't support IReactorProcess",
)
@skipIf(runtime.platform.getType() != "posix", "Only runs on POSIX platform")
@skipIf(
    not interfaces.IReactorProcess(reactor, None),
    "reactor doesn't support IReactorProcess",
)
        if self.verbose:
            print("kill [%d] with SIGTERM" % num)
        if self.verbose:
            print(self.pp[0].finished, self.pp[1].finished)
        if self.verbose:
            print("starting processes")
        if self.verbose:
            print("starting processes")
        if self.verbose:
            print("starting processes")
                self.fail("read '%s' on fd %d (not 1) during state 1" % (childFD, data))
            # print "len", len(self.data)
                    self.fail("got '%s' on fd1, expected 'righto'" % self.data)
                # print "state2", self.state
            self.fail(f"read '{childFD}' on fd {data} during state 2")
                self.fail(f"read '{childFD}' on fd {data} (not 1) during state 3")
                    self.fail("got '%s' on fd1, expected 'closed'" % self.data)
            self.fail(f"read '{childFD}' on fd {data} during state 4")
                self.fail("got connectionLost(%d) (not 4) during state 2" % childFD)
@skipIf(runtime.platform.getType() != "posix", "Only runs on POSIX platform")
@skipIf(
    not interfaces.IReactorProcess(reactor, None),
    "reactor doesn't support IReactorProcess",
)
        reactor.spawnProcess(
            p,
            pyExe,
            [pyExe, b"-u", b"-m", scriptPath],
            env=properEnv,
            childFDs={0: "w", 1: "r", 2: 2, 3: "w", 4: "r", 5: "w"},
        )
        d.addCallback(lambda x: self.assertFalse(p.failed, p.failed))
        reactor.spawnProcess(
            p,
            pyExe,
            [pyExe, b"-u", b"-m", scriptPath],
            env=properEnv,
            childFDs={1: "r", 2: 2},
        )

            self.assertEqual(p.outF.getvalue(), b"here is some text\ngoodbye\n")
        return d.addCallback(processEnded)
class PosixProcessBase:

        for loc in procutils.which(commandName):
            return FilePath(loc).asBytesMode().path

        binLoc = FilePath("/bin").child(commandName)
        usrbinLoc = FilePath("/usr/bin").child(commandName)
            return binLoc.asBytesMode().path
            return usrbinLoc.asBytesMode().path
                f"{commandName} found in neither standard location nor on PATH ({os.environ['PATH']})"
            )
        cmd = self.getCommand("true")
        reactor.spawnProcess(p, cmd, [b"true"], env=None, usePTY=self.usePTY)


        reactor.spawnProcess(
            p,
            pyExe,
            [pyExe, b"-c", b"import sys; sys.exit(1)"],
            env=None,
            usePTY=self.usePTY,
        )

        reactor.spawnProcess(
            p,
            pyExe,
            [pyExe, b"-u", "-m", scriptPath],
            env=properEnv,
            usePTY=self.usePTY,
        )
        return self._testSignal("HUP")
        return self._testSignal("INT")
        return self._testSignal("KILL")
        return self._testSignal("TERM")
    @skipIf(runtime.platform.isMacOSX(), "Test is flaky from a Darwin bug. See #8840.")
        cmd = self.getCommand("false")


            reactor.spawnProcess(p, cmd, [b"false"], env=None, usePTY=self.usePTY)


            ErrorInProcessEnded(),
            pyExe,
            env=properEnv,
            path=None,
        )



class MockSignal:

class MockOS:

        self.actions.append("setsid")
        self.actions.append(("fork", gc.isenabled()))
        self.actions.append(("read", fd, size))
        self.actions.append("exec")
        return -2 * self.pipeCount + 1, -2 * self.pipeCount
        self.actions.append(("exit", code))
        self.actions.append("waitpid")
        self.actions.append(("setuid", val))
        self.actions.append(("setgid", val))
        self.actions.append(("setregid", val1, val2))
        self.actions.append(("setreuid", val1, val2))
        self.actions.append(("switchuid", uid, gid))
        self.actions.append(("chdir", path))
        self.actions.append(("kill", pid, signalID))
        self.actions.append(("unlink", filename))
        self.actions.append(("umask", mask))
class DumbProcessWriter(ProcessWriter):
    """
    A fake L{ProcessWriter} used for tests.
    """

    def startReading(self):
        Here's the faking: don't do anything here.
class DumbProcessReader(ProcessReader):
    """
    A fake L{ProcessReader} used for tests.
    """

    def startReading(self):
        Here's the faking: don't do anything here.
class DumbPTYProcess(PTYProcess):
    """
    A fake L{PTYProcess} used for tests.
    """

    def startReading(self):
        Here's the faking: don't do anything here.

        cmd = b"/mock/ouch"
            reactor.spawnProcess(p, cmd, [b"ouch"], env=None, usePTY=False)
                self.mockos.actions, [("fork", False), "exec", ("exit", 1)]
            )
        cmd = b"/mock/ouch"
        reactor.spawnProcess(p, cmd, [b"ouch"], env=None, usePTY=False)
        self.assertEqual(set(self.mockos.closed), {-1, -4, -6})
        cmd = b"/mock/ouch"
        self.assertRaises(
            SystemError, reactor.spawnProcess, p, cmd, [b"ouch"], env=None, usePTY=True
        )
            self.mockos.actions, [("fork", False), "setsid", "exec", ("exit", 1)]
        )
        self.assertEqual(set(self.mockos.closed), {-1, -4, -6, -2, -3, -5})
        self.assertRaises(
            OSError,
            reactor.spawnProcess,
            protocol,
            None,
            childFDs={0: -10, 1: -11, 2: -13},
        )
        self.assertRaises(
            OSError,
            reactor.spawnProcess,
            protocol,
            None,
            childFDs={0: "r", 1: -11, 2: -13},
        )
        self.assertEqual(set(self.mockos.closed), {-1, -2})
        self.assertRaises(OSError, reactor.spawnProcess, protocol, None, usePTY=True)
        self.assertEqual(set(self.mockos.closed), {-12, -13})
        self.assertRaises(
            OSError, reactor.spawnProcess, protocol, None, usePTY=(-20, -21, "foo")
        )
        cmd = b"/mock/ouch"
            reactor.spawnProcess(p, cmd, [b"ouch"], env=None, usePTY=False)
                self.mockos.actions, [("fork", False), "exec", ("exit", 1)]
            )
        cmd = b"/mock/ouch"
            reactor.spawnProcess(p, cmd, [b"ouch"], env=None, usePTY=False, uid=8080)
                [
                    ("fork", False),
                    ("setuid", 0),
                    ("setgid", 0),
                    ("switchuid", 8080, 1234),
                    "exec",
                    ("exit", 1),
                ],
            )
        cmd = b"/mock/ouch"
        reactor.spawnProcess(p, cmd, [b"ouch"], env=None, usePTY=False, uid=8080)
        self.assertEqual(self.mockos.actions, [("fork", False), "waitpid"])
        cmd = b"/mock/ouch"
            reactor.spawnProcess(p, cmd, [b"ouch"], env=None, usePTY=True, uid=8081)
                [
                    ("fork", False),
                    "setsid",
                    ("setuid", 0),
                    ("setgid", 0),
                    ("switchuid", 8081, 1234),
                    "exec",
                    ("exit", 1),
                ],
            )
        cmd = b"/mock/ouch"
            reactor.spawnProcess(p, cmd, [b"ouch"], env=None, usePTY=True, uid=8080)
        self.assertEqual(self.mockos.actions, [("fork", False), "waitpid"])
        cmd = b"/mock/ouch"
        proc = reactor.spawnProcess(p, cmd, [b"ouch"], env=None, usePTY=False)
        cmd = b"/mock/ouch"
        proc = reactor.spawnProcess(p, cmd, [b"ouch"], env=None, usePTY=False)


        self.assertEqual(set(self.mockos.closed), {-4, -3, -2, -1})
        cmd = b"/mock/ouch"
        proc = reactor.spawnProcess(p, cmd, [b"ouch"], env=None, usePTY=False)
        self.assertEqual(
            self.mockos.actions,
            [("fork", False), "waitpid", ("kill", 21, signal.SIGKILL)],
        )
        cmd = b"/mock/ouch"
        proc = reactor.spawnProcess(p, cmd, [b"ouch"], env=None, usePTY=False)
        self.assertRaises(error.ProcessExitedAlready, proc.signalProcess, "KILL")
        cmd = b"/mock/ouch"
        proc = reactor.spawnProcess(p, cmd, [b"ouch"], env=None, usePTY=False)
        self.assertRaises(error.ProcessExitedAlready, proc.signalProcess, "KILL")
        cmd = b"/mock/ouch"
        proc = reactor.spawnProcess(p, cmd, [b"ouch"], env=None, usePTY=False)
        err = self.assertRaises(OSError, proc.signalProcess, "KILL")
@skipIf(runtime.platform.getType() != "posix", "Only runs on POSIX platform")
@skipIf(
    not interfaces.IReactorProcess(reactor, None),
    "reactor doesn't support IReactorProcess",
)
        reactor.spawnProcess(
            p,
            pyExe,
            [
                pyExe,
                b"-c",
                networkString("import sys; sys.stderr.write" "('{}')".format(value)),
            ],
            env=None,
            path="/tmp",
            usePTY=self.usePTY,
        )
        return d.addCallback(processEnded)
        cmd = self.getCommand("gzip")
        reactor.spawnProcess(
            p, cmd, [cmd, b"-c"], env=None, path="/tmp", usePTY=self.usePTY
        )
        return d.addCallback(processEnded)
@skipIf(runtime.platform.getType() != "posix", "Only runs on POSIX platform")
@skipIf(
    not interfaces.IReactorProcess(reactor, None),
    "reactor doesn't support IReactorProcess",
)

        reactor.spawnProcess(
            p,
            pyExe,
            [pyExe, b"-u", b"-m", scriptPath],
            env=properEnv,
            usePTY=self.usePTY,
        )
                error.ProcessExitedAlready, p.transport.signalProcess, "HUP"
            )
                (
                    "Error message from process_tty "
                    "follows:\n\n%s\n\n" % (p.outF.getvalue(),)
                ),
            )
        return d.addCallback(processEnded)
        self.assertRaises(
            ValueError,
            reactor.spawnProcess,
            p,
            pyExe,
            pyArgs,
            usePTY=1,
            childFDs={1: b"r"},
        )
            return self.deferred.errback(ValueError(f"wrong termination: {reason}"))
            return self.deferred.errback(ValueError(f"Wrong exit code: {v.exitCode}"))
@skipIf(runtime.platform.getType() != "win32", "Only runs on Windows")
@skipIf(
    not interfaces.IReactorProcess(reactor, None),
    "reactor doesn't support IReactorProcess",
)
        return d.addCallback(processEnded)
        import win32api  # type: ignore[import]
        env = dict(os.environ)
            sys.getfilesystemencoding()
        )
        pyExe = FilePath(sys.executable).path
        args = [pyExe, "-u", "-m", "twisted.test.process_stdinreader"]
        env["PYTHONPATH"] = pythonPath
        self.assertRaises(ValueError, reactor.spawnProcess, p, pyExe, pyArgs, uid=1)
        self.assertRaises(ValueError, reactor.spawnProcess, p, pyExe, pyArgs, gid=1)
        self.assertRaises(ValueError, reactor.spawnProcess, p, pyExe, pyArgs, usePTY=1)
        self.assertRaises(
            ValueError, reactor.spawnProcess, p, pyExe, pyArgs, childFDs={1: "r"}
        )
        reactor.spawnProcess(p, pyExe, [pyExe, b"-u", b"-m", scriptPath], env=properEnv)
        return self._testSignal("TERM")
        return self._testSignal("INT")
        return self._testSignal("KILL")


            self.assertRaises(
                win32api.error, win32api.GetHandleInformation, self.hProcess
            )
            self.assertRaises(
                win32api.error, win32api.GetHandleInformation, self.hThread
            )

@skipIf(runtime.platform.getType() != "win32", "Only runs on Windows")
@skipIf(
    not interfaces.IReactorProcess(reactor, None),
    "reactor doesn't support IReactorProcess",
)
    def test_AsciiEncodeableUnicodeEnvironment(self):
        C{os.environ} (inherited by every subprocess on Windows)
        contains Unicode keys and Unicode values which can be ASCII-encodable.
        os.environ["KEY_ASCII"] = "VALUE_ASCII"
        self.addCleanup(operator.delitem, os.environ, "KEY_ASCII")

        p = GetEnvironmentDictionary.run(reactor, [], os.environ)

        def gotEnvironment(environb):
            self.assertEqual(environb[b"KEY_ASCII"], b"VALUE_ASCII")
    @skipIf(
        sys.stdout.encoding != sys.getfilesystemencoding(),
        "sys.stdout.encoding: {} does not match "
        "sys.getfilesystemencoding(): {} .  May need to set "
        "PYTHONUTF8 and PYTHONIOENCODING environment variables.".format(
            sys.stdout.encoding, sys.getfilesystemencoding()
        ),
    )
    def test_UTF8StringInEnvironment(self):
        """
        L{os.environ} (inherited by every subprocess on Windows) can
        contain a UTF-8 string value.
        """
        envKey = "TWISTED_BUILD_SOURCEVERSIONAUTHOR"
        envKeyBytes = b"TWISTED_BUILD_SOURCEVERSIONAUTHOR"
        envVal = "Speciał Committór"
        os.environ[envKey] = envVal
        self.addCleanup(operator.delitem, os.environ, envKey)

        p = GetEnvironmentDictionary.run(reactor, [], os.environ)

        def gotEnvironment(environb):
            self.assertIn(envKeyBytes, environb)
            self.assertEqual(
                environb[envKeyBytes], "Speciał Committór".encode(sys.stdout.encoding)
            )

        return p.getResult().addCallback(gotEnvironment)
@skipIf(runtime.platform.getType() != "win32", "Only runs on Windows")
@skipIf(
    not interfaces.IReactorProcess(reactor, None),
    "reactor doesn't support IReactorProcess",
)


        scriptPath = FilePath(__file__).sibling("process_cmdline.py").path
        pyExe = FilePath(sys.executable).path
        comspec = "cmd.exe"
        cmd = [comspec, "/c", pyExe, scriptPath]
        p = _dumbwin32proc.Process(reactor, processProto, None, cmd, {}, None)
        return d.addCallback(pidCompleteCb)

@skipIf(runtime.platform.getType() != "win32", "Only runs on Windows")
@skipIf(
    not interfaces.IReactorProcess(reactor, None),
    "reactor doesn't support IReactorProcess",
)
        r"""

        def fakeCreateprocess(
            appName,
            commandLine,
            processAttributes,
            threadAttributes,
            bInheritHandles,
            creationFlags,
            newEnvironment,
            currentDirectory,
            startupinfo,
        ):
            return realCreateProcess(
                appName,
                commandLine,
                processAttributes,
                threadAttributes,
                bInheritHandles,
                creationFlags,
                newEnvironment,
                currentDirectory,
                startupinfo,
            )

        self.patch(_dumbwin32proc.win32process, "CreateProcess", fakeCreateprocess)
        self.assertEqual(flags, [_dumbwin32proc.win32process.CREATE_NO_WINDOW])

        for name, mode in [
            (j(self.foobaz, "executable"), 0o700),
            (j(self.foo, "executable"), 0o700),
            (j(self.bazfoo, "executable"), 0o700),
            (j(self.bazfoo, "executable.bin"), 0o700),
            (j(self.bazbar, "executable"), 0),
        ]:
        self.oldPath = os.environ.get("PATH", None)
        os.environ["PATH"] = os.pathsep.join(
            (self.foobar, self.foobaz, self.bazfoo, self.bazbar)
        )
                del os.environ["PATH"]
            os.environ["PATH"] = self.oldPath
        del os.environ["PATH"]
        expectedPaths = [j(self.foobaz, "executable"), j(self.bazfoo, "executable")]
        old = os.environ.get("PATHEXT", None)
        os.environ["PATHEXT"] = os.pathsep.join((".bin", ".exe", ".sh"))
                del os.environ["PATHEXT"]
                os.environ["PATHEXT"] = old
        expectedPaths = [
            j(self.foobaz, "executable"),
            j(self.bazfoo, "executable"),
            j(self.bazfoo, "executable.bin"),
        ]
    output = b""
    errput = b""
@skipIf(
    not interfaces.IReactorProcess(reactor, None),
    "reactor doesn't support IReactorProcess",
)
            p,
            pyExe,
            [
                pyExe,
                b"-u",
                b"-c",
                networkString(
                    "input()\n"
                    "import sys, os, time\n"
                    # Give the system a bit of time to notice the closed
                    # descriptor.  Another option would be to poll() for HUP
                    # instead of relying on an os.write to fail with SIGPIPE.
                    # However, that wouldn't work on macOS (or Windows?).
                    "for i in range(1000):\n"
                    '    os.write(%d, b"foo\\n")\n'
                    "    time.sleep(0.01)\n"
                    "sys.exit(42)\n" % (fd,)
                ),
            ],
            env=None,
        )
        p.transport.write(b"go\n")
        self.assertNotEqual(reason.exitCode, 42, "process reason was %r" % reason)
        self.assertEqual(p.output, b"")

            if runtime.platform.isWindows():
                self.assertIn(b"OSError", errput)
                self.assertIn(b"22", errput)
                self.assertIn(b"BrokenPipeError", errput)
            if runtime.platform.getType() != "win32":
                self.assertIn(b"Broken pipe", errput)


            self.assertEqual(errput, b"")
