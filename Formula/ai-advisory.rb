class AiAdvisory < Formula
  include Language::Python::Virtualenv

  desc "Query multiple LLMs and run consensus evaluation via OpenRouter API"
  homepage "https://github.com/yourusername/ai-advisory"
  url "https://github.com/yourusername/ai-advisory/archive/refs/tags/v0.1.0.tar.gz"
  sha256 "" # Will be filled when creating a release
  license "MIT"

  depends_on "python@3.11"

  resource "typer" do
    url "https://files.pythonhosted.org/packages/typer/typer-0.21.2.tar.gz"
    sha256 "" # Add actual sha256
  end

  resource "httpx" do
    url "https://files.pythonhosted.org/packages/httpx/httpx-0.28.1.tar.gz"
    sha256 "" # Add actual sha256
  end

  resource "rich" do
    url "https://files.pythonhosted.org/packages/rich/rich-14.3.2.tar.gz"
    sha256 "" # Add actual sha256
  end

  def install
    virtualenv_install_with_resources
  end

  test do
    assert_match "ai-advisory", shell_output("#{bin}/ai-advisory --help")
  end
end
